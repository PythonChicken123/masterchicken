const fs = require('fs');
const csv = require('csv-parser');

fs.createReadStream('map/map.csv')
  .pipe(csv())
  .on('data', (row) => {
    console.log(row);
  })
  .on('end', () => {
    console.log('CSV file successfully processed.');
  });
