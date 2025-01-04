from flask import Flask, render_template

app = Flask(__name__)

# Sample product data
products = [
    {
        'id': 1,
        'name': 'Laptop',
        'price': 999.99,
        'image': 'static/images/laptop.jpg',
        'description': 'High-performance laptop with 16GB RAM and 512GB SSD.'
    },
    {
        'id': 2,
        'name': 'Smartphone',
        'price': 699.99,
        'image': 'static/images/smartphone.jpg',
        'description': 'Latest smartphone with 128GB storage and 48MP camera.'
    },
    {
        'id': 3,
        'name': 'Headphones',
        'price': 199.99,
        'image': 'static/images/headphones.jpg',
        'description': 'Noise-cancelling headphones with 20-hour battery life.'
    }
]

@app.route('/')
def home():
    return render_template('index.html', products=products)

@app.route('/product/<int:product_id>')
def product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        return render_template('product.html', product=product)
    return "Product not found", 404

if __name__ == '__main__':
    app.run(debug=True)