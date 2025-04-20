function processOrder(order) {
  if (order.status === 'pending') {
      console.log("Processing order...");
      // do stuff
  }
  if (order.status === 'shipped') {
      console.log("Already shipped.");
  }
}
