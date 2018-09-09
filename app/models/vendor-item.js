import DS from 'ember-data';
import { computed } from '@ember/object'

export default DS.Model.extend({
  name: DS.attr(),
  timerStartedAt: DS.attr(),
  timerStopAt: DS.attr()
});
