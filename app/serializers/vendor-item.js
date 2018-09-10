import DS from 'ember-data';

export default DS.JSONAPISerializer.extend({

  attrs: {
    timerStartedAt: 'timer_started_at',
    timerStopAt: 'timer_stop_at'
  }

});
