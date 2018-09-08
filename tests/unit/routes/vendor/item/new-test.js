import { module, test } from 'qunit';
import { setupTest } from 'ember-qunit';

module('Unit | Route | vendor/item/new', function(hooks) {
  setupTest(hooks);

  test('it exists', function(assert) {
    let route = this.owner.lookup('route:vendor/item/new');
    assert.ok(route);
  });
});
