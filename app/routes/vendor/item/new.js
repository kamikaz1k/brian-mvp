import Route from '@ember/routing/route';
import moment from 'moment';

export default Route.extend({

  model() {
    return {
      name: "",
      duration: 120
    }
  },

  actions: {
    saveItem(item) {
      let startedAt = moment();
      this.store.createRecord('vendor-item', {
        name: item.name,
        timerStartedAt: startedAt.toISOString(),
        timerStopAt: startedAt.add(item.duration, 'seconds').toISOString()
      });
      this.transitionTo('vendor.index');
    }
  }

});
