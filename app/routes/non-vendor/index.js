import Route from '@ember/routing/route';

export default Route.extend({

    model() {
        return {
            vendors: [
                // {name: , status: }
                {name: "Burger Shack", status: "Open"},
                {name: "Woofle House", status: "Open"},
                {name: "Tea & Friends", status: "Closed"}
            ]
        }
    }

});
