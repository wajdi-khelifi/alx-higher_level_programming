class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }
  print () {
    for (let i = 0; i < this.height; i++) {
      let r = '';
      for (let j = 0; j < this.width; j++) {
        r += 'X';
      }
      console.log(r);
    }
  }
  rotate () {
    const tmp = this.height;
    this.height = this.width;
    this.width = tmp;
  }
  double () {
    this.height *= 2;
    this.width *= 2;
  }
}
module.exports = Rectangle; /*This is a special object in Node.
js modules that is used to expose functionality from one module to another.
Anything assigned to module.exports will be available for other modules to import.*/
