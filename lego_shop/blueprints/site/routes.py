from flask import Blueprint, flash, redirect, render_template, request

#internal import
from lego_shop.models import Product, Customer, Order, db
from lego_shop.forms import ProductForm, SearchForm
from lego_shop.helpers import gimme_legos



site = Blueprint('site', __name__, template_folder='site_templates')

#use site object to create our routes
@site.route('/', methods=["GET", "POST"])
def shop():
    form = SearchForm()
    allprods = Product.query.all() #the same as SELECT * FROM products, list of objects
    allcustomers = Customer.query.all()
    allorders = Order.query.all()
    shop_stats = {
        'products' : len(allprods), #total products
        'sales' : sum([order.order_total for order in allorders]), #[27.99, 43.99, 50.99] sum of orders
        'customers' : len(allcustomers)
    }
    if request.method=="POST" and form.validate_on_submit():
        legos=gimme_legos(form.name.data)
        print(legos)
        data=legos['results']#we need to access the key of results
        return render_template('shop.html', shop=allprods, stats=shop_stats, form=form, data=data)
   

    #dict for our shop stats/info

    

                    #in render_template: left sdie html, right side our route
    return render_template('shop.html', shop=allprods, stats=shop_stats, form=form)#no data=data

@site.route('/shop/create', methods= ['GET', 'POST'])
def create():

    #instantiate our productionform

    createform = ProductForm()

    if request.method == 'POST' and createform.validate_on_submit():
        #grab our data from our form
        name = createform.name.data
        image = createform.image.data
        description = createform.description.data
        price = createform.price.data
        quantity = createform.quantity.data

        #instantiate that class as an object passing in our arguments to replace our parameters
        product = Product(name, price, quantity, image, description)

        db.session.add(product)
        db.session.commit()

        flash(f"You have succesfully created product {name}", category='success')
        return redirect('/')
    
    elif request.method == 'POST':
        flash("We can't process your request", category='warning')
        return redirect('/shop/create')
    
    return render_template('create.html', form=createform )

@site.route('/shop/update/<id>', methods=['GET', 'POST']) #<PARAMETER> this is how pass parameters to our routes
def update(id):

    #lets grab our specific product we want to update
    product = Product.query.get(id) #this should only ever bring back 1 item/object
    updateform = ProductForm()

    if request.method == 'POST' and updateform.validate_on_submit():

        product.name = updateform.name.data
        product.image = updateform.image.data
        product.description = updateform.description.data
        product.price = updateform.price.data
        product.quantity = updateform.quantity.data

        db.session.commit()

        flash(f"You have successfully updated product {product.name}", category='success')
        return redirect('/')
    
    elif request.method == 'POST':
        flash("We were unable to process your request", category='warning')
        return redirect('/')
    
    return render_template('update.html', form=updateform, product=product )

@site.route('/shop/delete/<id>')
def delete(id):

    #query our database to find that object we want to delete
    product = Product.query.get(id)

    db.session.delete(product)
    db.session.commit()

    return redirect('/')