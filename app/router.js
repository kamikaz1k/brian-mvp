import EmberRouter from '@ember/routing/router';
import config from './config/environment';

const Router = EmberRouter.extend({
  location: config.locationType,
  rootURL: config.rootURL
});

Router.map(function() {
  this.route('login');
  this.route('vendor', function() {
    this.route('item', function() {
      this.route('new');
    });
  });
  this.route('non-vendor', function() {
    this.route('vendor', function() {
      this.route('show', { path: '/:vendor_id' });
    });
  });
});

export default Router;
