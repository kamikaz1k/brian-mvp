import Route from '@ember/routing/route';

export default Route.extend({

  model(params) {
    return {
      vendor: this.store.findRecord(
        'vendor',
        params.vendor_id,
        { include: 'vendor-items' }
      )
    }
  }

});
