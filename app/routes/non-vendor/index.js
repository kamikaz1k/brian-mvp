import Route from '@ember/routing/route';

export default Route.extend({

    model() {
        return {
            vendors: this.store.findAll('vendor')
        }
    },

    afterModel(model) {
        if (model.vendors.length === 0) {
            model.vendors = [
                {name: "Burger Shack", status: "Open"},
                {name: "Woofle House", status: "Open"},
                {name: "Tea & Friends", status: "Closed"}
            ].map(v => this.store.createRecord('vendor', v));
        }
    }

});
