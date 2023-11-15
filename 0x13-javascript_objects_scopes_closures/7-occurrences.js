#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  const counter = function (count, value) {
    count += (value === searchElement) ? 1 : 0;
    return count;
  };
  return list.reduce(counter, 0);
};
