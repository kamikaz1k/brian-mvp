import Route from '@ember/routing/route';

export default Route.extend({

    model() {
        return {
            items: this.store.findAll('vendor-item')
            // items: [
            //     // {name: , timer: }
            //     /* timer should be a computed property that keeps incrementing*/
            //     {name: "Burgers", timer: 123},
            //     {name: "Rotis", timer: 77},
            //     {name: "Lassi", timer: 987}
            // ]
        }
    },

    actions: {
        showTimer() {
            alert("show timer");
        }
    }
});
