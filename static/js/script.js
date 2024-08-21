document.addEventListener('DOMContentLoaded', () => {
    console.log("HaveABreak Coffee Shop website loaded!");

    // Sample data (replace with dynamic content from Flask)
    const coffees = [
        { name: 'Espresso', price_s: 15.00, price_m: 30.00, price_l: 50.00 },
        { name: 'Cold Brew', price_s: 15.00, price_m: 30.00, price_l: 50.00 },
        { name: 'Matcha', price_s: 15.00, price_m: 30.00, price_l: 50.00 },
        { name: 'Latte (Caramel or Vanilla)', price_s: 15.00, price_m: 30.00, price_l: 50.00 },
        { name: 'Mocha', price_s: 15.00, price_m: 30.00, price_l: 50.00 },
        { name: 'Black Coffee', price_s: 15.00, price_m: 30.00, price_l: 50.00 },
        { name: 'Cappuccino', price_s: 15.00, price_m: 30.00, price_l: 50.00 },
    ];

    const desserts = [
        { name: 'Ice Cream Waffles', price: 50.00 },
        { name: 'Cheesecake', price: 50.00 },
        { name: 'Caramel Cupcake', price: 50.00 },
        { name: 'Strawberry Cupcake', price: 50.00 },
        { name: 'White Cream Cupcake', price: 50.00 },
        { name: 'Lotus Biscuits', price: 50.00 },
    ];

    const coffeeContainer = document.querySelector('#coffees .menu-items');
    const dessertContainer = document.querySelector('#desserts .menu-items');

    coffees.forEach(coffee => {
        const item = document.createElement('div');
        item.className = 'menu-item';
        item.innerHTML = `
            <h3>${coffee.name}</h3>
            <p>Small: ${coffee.price_s} TRY</p>
            <p>Medium: ${coffee.price_m} TRY</p>
            <p>Large: ${coffee.price_l} TRY</p>
        `;
        coffeeContainer.appendChild(item);
    });

    desserts.forEach(dessert => {
        const item = document.createElement('div');
        item.className = 'menu-item';
        item.innerHTML = `
            <h3>${dessert.name}</h3>
            <p>Price: ${dessert.price} TRY</p>
        `;
        dessertContainer.appendChild(item);
    });
});

document.querySelectorAll('.add-to-cart').forEach(button => {
    button.addEventListener('click', function(event) {
        event.preventDefault();
        const productId = this.dataset.productId;
        const sizeDropdown = this.previousElementSibling.previousElementSibling; // Selects the dropdown
        const selectedSize = sizeDropdown.value;
        
        // Redirect to the backend with the selected size and product id
        window.location.href = `/add-to-cart/${productId}/coffee/${selectedSize}`;
    });
});

