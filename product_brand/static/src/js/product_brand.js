odoo.define('product_brand.brand_id', function(require){
    'use strict';
    console.log("check......");
    var models = require('point_of_sale.models');

    var _super_orderline = models.Orderline.prototype;
    console.log("models..", models);
    models.load_fields('product.product', 'brand_id')
    models.Orderline = models.Orderline.extend({
        initialize:function(attr,options){
            var line = _super_orderline.initialize.apply(this,arguments);
            this.brand_id = this.product.brand_id;
            console.log("brand_id", this.brand_id);
        }



    })
})
