import { module, test } from 'qunit';
import { setupTest } from 'ember-qunit';

module('Unit | Route | non-vendor/vendor/show', function(hooks) {
  setupTest(hooks);

  test('it exists', function(assert) {
    let route = this.owner.lookup('route:non-vendor/vendor/show');
    assert.ok(route);
  });
});
