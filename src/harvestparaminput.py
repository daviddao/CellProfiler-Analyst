import wx
import sys
import wx.lib.mixins.listctrl as listmix
from experimentsettings import *
from vesselpanel import VesselPanel, VesselScroller
from reseeddialog import *

ID_RESEED = wx.NewId()

########################################################################        
########       Popup Dialog showing all instances of stock culture   ####
########################################################################            
class HarvestDialog(wx.Dialog):
    def __init__(self, parent, harvested_platewells, selected_timepoint):
        wx.Dialog.__init__(self, parent, -1, size=(250,300), style=wx.DEFAULT_DIALOG_STYLE|wx.RESIZE_BORDER)
        
        self.settings_controls = {}        
        meta = ExperimentSettings.getInstance()
        self.harvested_platewells = harvested_platewells
        self.selected_timepoint = selected_timepoint
        
        cellload_list = meta.get_field_instances('CellTransfer|Seed|')
        cellharvest_list = meta.get_field_instances('CellTransfer|Harvest|')
        
        if cellharvest_list:
            self.harvest_instance  =  int(cellharvest_list[-1])+1
        else:
            self.harvest_instance = 1
        
        if cellload_list:
            self.harvested_pw_info = {}
            
            for seed_instnace in cellload_list:
                timepoints =  meta.get_field('CellTransfer|Seed|EventTimepoint|'+str(seed_instnace), default='')
                for timepoint in timepoints:                
                    seeded_pws = meta.get_field('CellTransfer|Seed|Wells|'+str(seed_instnace)+'|'+str(timepoint), default='')
                    for seeded_pw in seeded_pws:
                        if seeded_pw in self.harvested_platewells:                             
                            #TO DO check for conflict of multiple seeding instace
                            # and check for already NOT been harvested
                            self.stockInstance = meta.get_field('CellTransfer|Seed|StockInstance|%s'%str(seed_instnace), default='')
                            # from stock                            
                            self.harvested_pw_info['Cell Line'] = meta.get_field('StockCulture|Sample|CellLine|%s'%str(self.stockInstance), default = '')
                            self.harvested_pw_info['ACTT Reference'] = meta.get_field('StockCulture|Sample|ATCCref|%s'%str(self.stockInstance), default = '')
                            self.harvested_pw_info['Organism'] = meta.get_field('StockCulture|Sample|Organism|%s'%str(self.stockInstance), default = '')
                            # from seeded wells
                            self.harvested_pw_info['Harvest Density'] = meta.get_field('CellTransfer|Seed|SeedingDensity|%s'%str(seed_instnace), default = '')
                            self.harvested_pw_info['Medium Used'] = meta.get_field('CellTransfer|Seed|MediumUsed|%s'%str(seed_instnace), default = '')
                            self.harvested_pw_info['Medium Additives'] = meta.get_field('CellTransfer|Seed|MediumAddatives|%s'%str(seed_instnace), default = '')
                            self.harvested_pw_info['Trypsinizatiton'] = meta.get_field('CellTransfer|Seed|Trypsinizatiton|%s'%str(seed_instnace), default = '')
            
        
        
        #create the GUI
        fgs = wx.FlexGridSizer(rows=15, cols=2, hgap=5, vgap=5) 
        # immutable parameters from stock reference
        fgs.Add(wx.StaticText(self, -1, 'Cell Line'), 0)
        fgs.Add(wx.StaticText(self, -1, self.harvested_pw_info['Cell Line']), 0)
        fgs.Add(wx.StaticText(self, -1, 'ATCC Reference'), 0)
        fgs.Add(wx.StaticText(self, -1, self.harvested_pw_info['ACTT Reference']), 0)
        fgs.Add(wx.StaticText(self, -1, 'Organism'), 0)
        fgs.Add(wx.StaticText(self, -1, self.harvested_pw_info['Organism']), 0)
        # parameters regarding selected Wells and timepoint
        meta.set_field('CellTransfer|Harvest|StockInstance|%s'%self.harvest_instance,  self.stockInstance)
        meta.set_field('CellTransfer|Harvest|Wells|%s|%s'%(self.harvest_instance, self.selected_timepoint),   set(self.harvested_platewells))
        meta.set_field('CellTransfer|Harvest|EventTimepoint|%s'%self.harvest_instance,    self.selected_timepoint)
        
        # Seeding Density
        harvestTAG = 'CellTransfer|Harvest|Density|'+str(self.harvest_instance)
        self.settings_controls[harvestTAG] = wx.TextCtrl(self, value=self.harvested_pw_info['Harvest Density'])
        self.settings_controls[harvestTAG].Bind(wx.EVT_TEXT, self.OnSavingData)
        self.settings_controls[harvestTAG].SetToolTipString('Number of cells harvested from each well or flask')
        fgs.Add(wx.StaticText(self, -1, 'Harvesting Density'), 0)
        fgs.Add(self.settings_controls[harvestTAG], 0, wx.EXPAND)

        # Medium Used
        medmTAG = 'CellTransfer|Harvest|MediumUsed|'+str(self.harvest_instance)
        self.settings_controls[medmTAG] = wx.Choice(self, -1,  choices=['Typical', 'Atypical'])
        self.settings_controls[medmTAG].SetStringSelection(self.harvested_pw_info['Medium Used'])
        self.settings_controls[medmTAG].Bind(wx.EVT_CHOICE, self.OnSavingData)
        self.settings_controls[medmTAG].SetToolTipString('Typical/Atypical (Ref in both cases)')
        fgs.Add(wx.StaticText(self, -1, 'Medium Used'), 0)
        fgs.Add(self.settings_controls[medmTAG], 0, wx.EXPAND) 

        #  Medium Addatives
        medaddTAG = 'CellTransfer|Harvest|MediumAddatives|'+str(self.harvest_instance)
        self.settings_controls[medaddTAG] = wx.TextCtrl(self, value=self.harvested_pw_info['Medium Additives'])
        self.settings_controls[medaddTAG].Bind(wx.EVT_TEXT, self.OnSavingData)
        self.settings_controls[medaddTAG].SetToolTipString('Any medium addatives used with concentration, Glutamine')
        fgs.Add(wx.StaticText(self, -1, 'Medium Additives'), 0)
        fgs.Add(self.settings_controls[medaddTAG], 0, wx.EXPAND)

        # Trypsinization
        trypsTAG = 'CellTransfer|Harvest|Trypsinizatiton|'+str(self.harvest_instance)
        self.settings_controls[trypsTAG] = wx.Choice(self, -1,  choices=['Yes', 'No'])
        self.settings_controls[trypsTAG].SetStringSelection(self.harvested_pw_info['Trypsinizatiton'])
        self.settings_controls[trypsTAG].Bind(wx.EVT_CHOICE, self.OnSavingData)
        self.settings_controls[trypsTAG].SetToolTipString('(Y/N) After cells were loded on the exerimental vessel, i.e. time 0 of the experiment')
        fgs.Add(wx.StaticText(self, -1, 'Trypsinization'), 0)
        fgs.Add(self.settings_controls[trypsTAG], 0, wx.EXPAND) 
        
        #Buttons    
        data_acqs_btn = wx.Button(self, wx.ID_OK, 'Data Acquisition')
        reseed_btn = wx.Button(self, ID_RESEED, 'Reseed')
        reseed_btn.Bind(wx.EVT_BUTTON, self.onReseed)
        
        fgs.Add(data_acqs_btn, 0, wx.ALL, 5)
        fgs.Add(reseed_btn, 0, wx.ALL, 5)
        #---------------Layout with sizers---------------
        self.Sizer = wx.BoxSizer(wx.VERTICAL)
        self.Sizer.Add(fgs, 1, wx.EXPAND|wx.ALL, 5)
        
    def onReseed(self, event):
        reseed_dialog = ReseedDialog(self, self.harvest_instance, self.selected_timepoint)
        reseed_dialog.ShowModal()
        self.Destroy()

    def OnSavingData(self, event):
        meta = ExperimentSettings.getInstance()

        ctrl = event.GetEventObject()
        tag = [t for t, c in self.settings_controls.items() if c==ctrl][0]
        if isinstance(ctrl, wx.Choice):
            meta.set_field(tag, ctrl.GetStringSelection())
        else:
            meta.set_field(tag, ctrl.GetValue())
     
        