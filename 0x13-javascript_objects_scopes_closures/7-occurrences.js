#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let nbOccurences = 0;
    for (let i = 0; i < list.lenght; i++) {
      if (searchElement === list[i]) {
        nbOccurences++;
      }
    }
    return nbOccurences;
};
