ig.module( 
	'game.main' 
).requires(
	'impact.game',
	'impact.font'
).defines(function(){
	//$.get('')
	SavoG = ig.Game.extend({
		font: new ig.Font( 'media/04b03.font.png' ),
		init: function() {
			// Initialize your game here; bind keys etc.
		},
		update: function() {
			// Update all entities and backgroundMaps
			this.parent()
			// Add your own, additional update code here
		},
		draw: function() {
			// Draw all entities and backgroundMaps
			this.parent()
			//this.font.draw( 'User: '+user.nick, 10, 10, ig.Font.ALIGN.LEFT)
			this.font.draw( 'Development in progress!', 10, 10, ig.Font.ALIGN.LEFT)
		}
	})
	ig.main( '#game', SavoG, 60, 640, 370, 2) //1280, 720, 1)
})
