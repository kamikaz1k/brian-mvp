import Route from '@ember/routing/route';

export default Route.extend({

    model() {
        return {
            items: this.store.findAll('vendor-item')
        }
    }

});
