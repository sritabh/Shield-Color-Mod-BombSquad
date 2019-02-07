import random
import bs
from bsSpaz import *
import bsSpaz
bs.screenMessage("Shield ColorMod v2 By SobyDamn")
def equipShields(self, decay=False):
        """
        Give this spaz a nice energy shield.
        """

        if not self.node.exists():
            bs.printError('Can\'t equip shields; no node.')
            return
        
        factory = self.getFactory()
        if self.shield is None: 
            self.shield = bs.newNode('shield', owner=self.node,
                                     attrs={'color':self.node.color,
                                            'radius':1.3})
            self.node.connectAttr('positionCenter', self.shield, 'position')
        self.shieldHitPoints = self.shieldHitPointsMax = 650
        self.shieldDecayRate = factory.shieldDecayRate if decay else 0
        self.shield.hurt = 0
        bs.playSound(factory.shieldUpSound, 1.0, position=self.node.position)

        if self.shieldDecayRate > 0:
            self.shieldDecayTimer = bs.Timer(500, bs.WeakCall(self.shieldDecay),
                                             repeat=True)
            self.shield.alwaysShowHealthBar = True # so user can see the decay
bsSpaz.Spaz.equipShields = equipShields


