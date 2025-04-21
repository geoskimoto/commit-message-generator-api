function calculateTotal(items, applyDiscount = false) {
    let total = 0;

    // Sum up all item prices
    for (let item of items) {
        total += item.price;
    }

    // Apply a 10% discount if requested
    if (applyDiscount) {
        total *= 0.9;
    }

    // Round to two decimal places
    return Math.round(total * 100) / 100;
}
