import DS from 'ember-data';
import { computed } from '@ember/object'

export default DS.Model.extend({
  name: DS.attr(),
  timerStartedAt: DS.attr(),
  timerStopAt: DS.attr(),
  timer: computed('timerStopAt', function() {
    return moment(this.get('timerStopAt')).diff(moment()) / 1000;
  })
});
