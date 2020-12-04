//Functions for creating dynamically rendered sections for value added content

function addSalt2Section(alertId, divId) {
  var sectionDiv = document.createElement('div')
  sectionDiv.classList.add = 'value-added-section';
  sectionDiv.id = 'salt2';

  var headerDiv = document.createElement('div')
  headerDiv.classList.add = 'section-header';
  sectionDiv.appendChild(headerDiv);

  var header = document.createElement('h3');
  header.textContent = 'Salt2 Supernova Fit';
  headerDiv.appendChild(header);

  var img = document.createElement("IMG");
  img.src = 'https://storage.googleapis.com/ardent-cycling-243415_ztf-sncosmo/salt2/plot_lc/candid_' + alertId + '.png';
  img.alt='';
  sectionDiv.appendChild(img);

  document.getElementById(divId).appendChild(sectionDiv);
}
