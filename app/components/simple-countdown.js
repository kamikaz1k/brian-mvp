import Component from '@ember/component';
import { computed } from '@ember/object';
import { equal } from '@ember/object/computed';
import moment from 'moment';

export default Component.extend({

  tagName: '',

  number: computed('endDateTime', 'checkedAt', function() {
    let diff = this.get('endDateTime').diff(this.get('checkedAt'))
    return Math.max(Math.round(diff / 1000), 0);
  }),

  isZero: equal('number', 0),

  checkedAt: moment(),

  endDateTimeString: null,

  endDateTime: computed('endDateTimeString', function() {
    return moment(this.get('endDateTimeString'));
  }),

  init() {
    this._super(...arguments);
    this.countdown();
  },

  countdown() {
    const id = requestAnimationFrame(() => {
      this.set('checkedAt', moment());
      this.countdown();
    });
    this.set('animationId', id);
  },

  willDestroyElement() {
    const id = this.get('animationId');
    if (id) {
      cancelAnimationFrame(id);
    }
  },

  actions: {
    reset() {
      this.set('finishAt', Date.now() + 5000);
    }
  }
});
