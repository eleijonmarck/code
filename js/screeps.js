for( var name in Game.creeps) {
	var creep = Game.creeps[name];

	if(creep.energy < creep.energyCapacity) {
				var sources = creep.room.find(Game.SOURCES);
						creep.moveTo(sources[0]);
						creep.harvest(sources[0]);									}
	else {
	creep.moveTo(Game.spawns.Spawn1);
	creep.transferEnergy(Game.spawns.Spawn1)							}												
}
