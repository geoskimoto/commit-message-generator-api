function handlePendingOrder(order) {
  console.log("Processing order...");
  // do stuff
}

function handleShippedOrder() {
  console.log("Already shipped.");
}

function processOrder(order) {
  switch(order.status) {
      case 'pending':
          handlePendingOrder(order);
          break;
      case 'shipped':
          handleShippedOrder();
          break;
      default:
          console.log("Unknown status.");
  }
}
