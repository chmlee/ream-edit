var div_with_random_id = function (h) {
  // Math.random should be unique because of its seeding algorithm.
  // Convert it to base 36 (numbers + letters), and grab the first 9 characters
  // after the decimal.
  id = '_' + Math.random().toString(36).substr(2, 9) + Math.random().toString(36).substr(2, 9)
  return "<div id='" + id + "' class='level-" + h[1] + "'>";
};
