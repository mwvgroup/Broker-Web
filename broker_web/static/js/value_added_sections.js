//Functions for creating dynamically rendered sections for value added content

function addSalt2Image(alertId, addToDivId) {
  let sectionDiv = document.createElement('div')
  sectionDiv.classList.add('value-added-section');
  sectionDiv.id = 'salt2';

  let headerDiv = document.createElement('div')
  headerDiv.classList.add('section-header');
  sectionDiv.appendChild(headerDiv);

  let header = document.createElement('h3');
  header.textContent = 'Salt2 Supernova Fit';
  headerDiv.appendChild(header);

  let img = document.createElement("IMG");
  img.src = 'https://storage.googleapis.com/ardent-cycling-243415_ztf-sncosmo/salt2/plot_lc/candid_' + alertId + '.png';
  img.alt='';
  sectionDiv.appendChild(img);

  document.getElementById(addToDivId).appendChild(sectionDiv);
  return img;
}

function addEmptySalt2Table(addToDivId, newTableId) {
  let colNames = [
      'Alert Id', 'Chisq', 'NDOF', 'z', 'z Err', 't0', 't0 Err', 'x0', 'x0 Err', 'x1', 'x1 Err', 'c', 'c Err'
  ];

  let fitResultTable = document.createElement('table')
  fitResultTable.classList.add("table")
  fitResultTable.classList.add("table-striped")
  fitResultTable.id = newTableId

  let thead = fitResultTable.createTHead();
  let row = thead.insertRow();
  for (let colNameText of colNames) {
    let th = document.createElement("th");
    let text = document.createTextNode(colNameText);
    th.appendChild(text);
    row.appendChild(th);
  }

  document.getElementById(addToDivId).appendChild(fitResultTable);
  return fitResultTable;
}
