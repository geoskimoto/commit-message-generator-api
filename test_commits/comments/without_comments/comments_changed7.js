function calculateTotal(items, applyDiscount = false) {
    let total = 0;
    for (let item of items) {
        total += item.price;
    }
    if (applyDiscount) {
        total *= 0.9;
    }
    return Math.round(total * 100) / 100;
}
