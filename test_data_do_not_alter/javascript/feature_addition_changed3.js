class Task {
  constructor(name) {
      this.name = name;
      this.completed = false;
      this.createdAt = new Date();
  }

  markComplete() {
      this.completed = true;
      this.completedAt = new Date();
  }
}
