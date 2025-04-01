from flask import Flask, jsonify, redirect, url_for
from flask.templating import render_template
import random
import math
import datetime
import uuid
import socket
import os
import time

# Version information
VERSION = "2.1"

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/order')
def process_order():

    def fake_heavy_computation():
        # Add some variability to processing time
        time.sleep(random.uniform(0.1, 0.5))
        num = random.randint(80_000, 130_000)
        _ = math.factorial(num)
        return True

    fake_heavy_computation()
    
    order_id = str(uuid.uuid4())
    
    # Updated product list with more modern tech products
    products = [
        "Quantum Processor", 
        "Neural Interface", 
        "Holographic Display", 
        "BioScanner", 
        "Anti-Gravity Module",
        "Fusion Battery",
        "Nanobot Swarm",
        "AI Assistant"
    ]
    
    order_items = []
    
    num_items = random.randint(1, 4)  # Increased max items
    order_total = 0
    
    for _ in range(num_items):
        product = random.choice(products)
        quantity = random.randint(1, 5)
        # Higher price points
        price = round(random.uniform(99.99, 999.99), 2)
        item_total = round(quantity * price, 2)
        order_total += item_total
        
        # Add product category
        categories = ["Computing", "Biotechnology", "Energy", "AI", "Quantum", "Communications"]
        
        order_items.append({
            "product": product,
            "category": random.choice(categories),
            "quantity": quantity,
            "price": price,
            "total": item_total
        })
    
    timestamp = datetime.datetime.now().isoformat()
    
    delivery_days = random.randint(1, 5)  # Faster delivery
    delivery_date = (datetime.datetime.now() + datetime.timedelta(days=delivery_days)).strftime("%Y-%m-%d")
    
    # Get server identification info
    hostname = socket.gethostname()
    try:
        ip_address = socket.gethostbyname(hostname)
    except:
        ip_address = "unknown"
    
    # Added service metrics
    processing_time = random.uniform(0.05, 0.3)
    
    response = {
        "_service": {
            "name": "SuperOrder Service",
            "version": VERSION,
            "processing_time_sec": round(processing_time, 4)
        },
        "_server": {
            "hostname": hostname,
            "ip": ip_address
        },
        "status": "Order Processed Successfully",
        "order_id": order_id,
        "timestamp": timestamp,
        "customer": {
            "id": f"CUST-{random.randint(10000, 99999)}",
            "tier": random.choice(["Standard", "Premium", "Enterprise"])
        },
        "items": order_items,
        "order_total": round(order_total, 2),
        "shipping": {
            "method": random.choice(["Standard", "Express", "Premium", "Same-Day"]),
            "carrier": random.choice(["SpaceX Logistics", "Quantum Transport", "Global Delivery Network"]),
            "estimated_delivery": delivery_date,
            "tracking_id": f"TRK-{uuid.uuid4().hex[:10].upper()}"
        },
        "payment": {
            "method": random.choice(["Credit Card", "PayPal", "Apple Pay", "Crypto", "Bank Transfer"]),
            "status": "Completed",
            "transaction_id": f"TX-{uuid.uuid4().hex[:8].upper()}"
        },
        "discounts": {
            "applied": random.choice([True, False]),
            "code": f"SUPER{random.randint(10, 99)}" if random.random() > 0.5 else None,
            "amount": round(order_total * random.uniform(0.05, 0.2), 2) if random.random() > 0.5 else 0
        }
    }
    
    return jsonify(response), 200

@app.errorhandler(404)
def page_not_found(_):
    return redirect(url_for('home'))

if __name__ == '__main__':
    print(f"Starting SuperOrder Service v{VERSION}")
    app.run(host='0.0.0.0', port=3000, debug=True)
