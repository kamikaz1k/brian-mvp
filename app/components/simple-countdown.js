import Component from '@ember/component';
import { inject } from '@ember/service';
import moment from 'moment';


import Ember from 'ember';

export default Component.extend({

  tagName: '',

  number: Ember.computed('endDateTime', 'checkedAt', function() {
    let diff = this.get('endDateTime').diff(this.get('checkedAt'))
    // (this.get('endDateTime') - this.get('checkedAt'))
    return Math.max(Math.round(diff / 1000), 0);
  }),

  isZero: Ember.computed.equal('number', 0),

  checkedAt: moment(),

  endDateTimeString: null,

  endDateTime: Ember.computed('endDateTimeString', function() {
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
