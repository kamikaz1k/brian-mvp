import DS from 'ember-data';

export default DS.Model.extend({

  name: DS.attr(),

  timerStartedAt: DS.attr(),

  timerStopAt: DS.attr()

});
