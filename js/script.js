const filter = document.getElementById('filter');
const filters = document.getElementsByClassName('check-button');
const filterTypes = ['class', 'color', 'range'];
checkboxes = {};
for (i of filterTypes) {
    checkboxes[i] = document.getElementsByClassName('check-button filter-' + i);
}
all_values = {};
for (const [type, group] of Object.entries(checkboxes)) {
    all_values[type] = [];
    for (checkbox of group) {
        all_values[type].push(checkbox.value);
    }
}

function changeFilter() {
    let checked = {};
    for (i of filterTypes) {
        checked[i] = [];
    }
    for (const filter of filters) {
        if (filter.checked) {
            const filterType = filter.dataset.filterType;
            checked[filterType].push(filter.value);
        }
    }
    for (let [key, value] of Object.entries(checked)) {
        value = value.length ? value : all_values[key];
        filter.setAttribute('data-filter-' + key, value.join(' '));
    }
}

for (let filter of filters) {
    filter.addEventListener('click', changeFilter);
}
changeFilter();
