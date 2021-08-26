const binarySearch = require("./binarySearchOccuranceSolution");

test("Testing the count of the first element in the array", () => {
  expect(binarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9], 1)["count"]).toBe(1);
});

test("Testing the count of the last element in the array", () => {
  expect(binarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9], 9)["count"]).toBe(1);
});

test("Testing the count of the second element in the array", () => {
  expect(
    binarySearch([1, 2, 3, 4, 4, 5, 5, 6, 6, 6, 7, 7, 7, 8, 9], 2)["count"]
  ).toBe(2);
});

test("Testing the count of the second to the last element in the array", () => {
  expect(
    binarySearch([1, 2, 3, 4, 4, 5, 5, 6, 6, 6, 7, 7, 7, 8, 9], 8)["count"]
  ).toBe(2);
});

test("Testing the number of counts of an item", () => {
  expect(
    binarySearch([1, 2, 3, 4, 4, 5, 5, 6, 6, 6, 7, 7, 7, 8, 9], 7)["count"]
  ).toBe(4);
});

test("Testing the number of occurance of an item", () => {
  expect(
    binarySearch([1, 2, 3, 4, 4, 5, 5, 6, 6, 6, 7, 7, 7, 8, 9], 7)["occurance"]
  ).toBe(3);
});

test("Testing the number for count", () => {
  expect(
    binarySearch([1, 2, 3, 4, 4, 5, 5, 6, 6, 6, 7, 7, 7, 8, 9], 6)["count"]
  ).toBe(3);
});

test("Testing the number for occurance", () => {
  expect(
    binarySearch([1, 2, 3, 4, 4, 5, 5, 6, 6, 6, 7, 7, 7, 8, 9], 6)["occurance"]
  ).toBe(3);
});

test("Testing the response for both occurance and count", () => {
  const response = binarySearch([0, 5, 10, 15, 20, 22, 30, 35, 40], 15);
  expect(response["occurance"]).toBe(1);
  expect(response["count"]).toBe(2);
});

test("Testing response when the item is not in the array", () => {
  const response = binarySearch([0, 5, 10, 15, 20, 22, 30, 35, 40], 11);
  expect(response["occurance"]).toBe(-1);
  expect(response["count"]).toBe(3);
});
