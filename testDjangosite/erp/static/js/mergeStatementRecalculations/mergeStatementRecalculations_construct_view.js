
buildStatementRecalculationsTbody();
setEventForButtons();

async function buildStatementRecalculationsTbody() {
    var data = await MergeStatementRecalculationsBusiness.getAllStatementList();
    var allForestData = await CommonBusiness.getAllForest();

    APP.subjectrf = allForestData.subjectrf;
    APP.forestly = allForestData.forestly;
    APP.district_forestly = allForestData.district_forestly;
    APP.quarter = allForestData.quarter;

    updateDataInStatementRecalculationsTbody(data);

    setEventForElementsFilter();
}

function updateDataInStatementRecalculationsTbody(data) {
    APP.idActiveItemTr = [];

    var tableBody = document.getElementById("statementRecalculations_tbody");
    var newHtml = "";

    for(var i = 0; i < data.length; i++) {

        data[i].subjectrf = CommonFunction.getSubjectNameByQuarterId(APP.subjectrf, data[i].id_subject_rf);
        data[i].forestly = CommonFunction.getForestlyNameByQuarterId(APP.forestly, data[i].id_forestly);
        data[i].district_forestly = CommonFunction.getDistrictForestlyNameByQuarterId(APP.district_forestly, data[i].id_district_forestly);
        data[i].quarter = CommonFunction.getQuarterNameByQuarterId(APP.quarter, data[i].id_quarter);

        let id = "statement_" + data[i].id;

        newHtml = newHtml + "<div>" + '<tr id="' + id + '" class="cursorPointer" onClick="addOrRemoveActiveItemTr(' + data[i].id + ')">' +
                            `<td class="textAlignCenter td1">${data[i].date}</td>
                            <td class="textAlignCenter td8">${data[i].id}</td>
                            <td class="td2">${data[i].subjectrf}</td>
                            <td class="td3">${data[i].forestly}</td>
                            <td class="td4">${data[i].district_forestly}</td>
                            <td class="textAlignCenter td5">${data[i].quarter}</td>
                            <td class="textAlignCenter td6">${data[i].soil_lot}</td>
                            <td class="textAlignCenter td7">${data[i].sample_region}</td>
                        </tr> \n` + "</div>";
    }
    tableBody.innerHTML = newHtml;
}

async function setEventForButtons() {
    document
        .querySelector("#merge_button")
        .addEventListener('click', async (e)=>{
            startMergeStatementRecalculations();
        });
}

async function startMergeStatementRecalculations() {
    if(APP.idActiveItemTr.length > 1) {
        let data = {
            id: APP.idActiveItemTr[0],
            ids: []
        }

        for(let i = 1; i < APP.idActiveItemTr.length; i++) {
            let item = {
                id: APP.idActiveItemTr[i]
            }
            data.ids.push(item);
        }

        await MergeStatementRecalculationsBusiness.mergeStatementRecalculations(data);

        let statementList = await MergeStatementRecalculationsBusiness.getAllStatementList();
        updateDataInStatementRecalculationsTbody(statementList);
        APP.idActiveItemTr = [];
    }
}

async function setEventForElementsFilter() {

    await setOptionInSubject();

    document
        .querySelector("#checkbox_filter_subject_rf")
        .addEventListener('click', async (e)=>{
            let subjectNode = document.querySelector("#filter_subject_rf");
            if(e.target.checked) {
                subjectNode.removeAttribute("disabled")
                subjectNode.addEventListener('change', async (e)=>{
                    await setOptionInForestly(MergeStatementRecalculationsBusiness.TypeData.BYID);
                });
                await setOptionInForestly(MergeStatementRecalculationsBusiness.TypeData.BYID);
            } else {
                subjectNode.setAttribute("disabled", "on");
                await setOptionInForestly(MergeStatementRecalculationsBusiness.TypeData.ALL);
            }
        });

    await setOptionInForestly(MergeStatementRecalculationsBusiness.TypeData.ALL);

    document
        .querySelector("#checkbox_filter_forestly")
        .addEventListener('click', async (e)=>{
            let forestlyNode = document.querySelector("#filter_forestly");
            if(e.target.checked) {
                forestlyNode.removeAttribute("disabled");
                forestlyNode.addEventListener('change', async (e)=>{
                    await setOptionInDistrictForestly(MergeStatementRecalculationsBusiness.TypeData.BYID);
                });
                await setOptionInDistrictForestly(MergeStatementRecalculationsBusiness.TypeData.BYID);
            } else {
                forestlyNode.setAttribute("disabled", "on");
                await setOptionInDistrictForestly(MergeStatementRecalculationsBusiness.TypeData.ALL);
            }
        });

    await setOptionInDistrictForestly(MergeStatementRecalculationsBusiness.TypeData.ALL);

    document
        .querySelector("#checkbox_filter_district_forestly")
        .addEventListener('click', async (e)=>{
            let districtForestly = document.querySelector("#filter_district_forestly");
            if(e.target.checked) {
                districtForestly.removeAttribute("disabled");
                districtForestly.addEventListener('change', async (e)=>{
                    await setOptionInQuarter(MergeStatementRecalculationsBusiness.TypeData.BYID);
                });
                await setOptionInQuarter(MergeStatementRecalculationsBusiness.TypeData.BYID);
            } else {
                districtForestly.setAttribute("disabled", "on");
                await setOptionInQuarter(MergeStatementRecalculationsBusiness.TypeData.ALL);
            }
        });

    await setOptionInQuarter(MergeStatementRecalculationsBusiness.TypeData.ALL);

    document
        .querySelector("#checkbox_filter_quartal")
        .addEventListener('click', (e)=>{
            if(e.target.checked) {
                document
                    .querySelector("#filter_quartal")
                    .removeAttribute("disabled");
            } else {
                document
                    .querySelector("#filter_quartal")
                    .setAttribute("disabled", "on");
            }
        });

    document
        .querySelector("#checkbox_filter_date_start")
        .addEventListener('click', (e)=>{
            if(e.target.checked) {
                document
                    .querySelector("#filter_date_start")
                    .removeAttribute("readonly");
            } else {
                document
                    .querySelector("#filter_date_start")
                    .setAttribute("readonly", "on");
            }
        });

    document
        .querySelector("#checkbox_filter_date_end")
        .addEventListener('click', (e)=>{
            if(e.target.checked) {
                document
                    .querySelector("#filter_date_end")
                    .removeAttribute("readonly");
            } else {
                document
                    .querySelector("#filter_date_end")
                    .setAttribute("readonly", "on");
            }
        });

    document
        .querySelector("#but_filtr")
        .addEventListener('click', async (e)=>{
            await searchByFilter();
        });
}

async function setOptionInSubject() {
    let subjects = await CommonBusiness.getAllSubjectrf();
    let subjectNode = document.querySelector("#filter_subject_rf");

    let newHtml = "";

    for(var i = 0; i < subjects.length; i++) {
        if(i == 0) {
            newHtml = newHtml + "<option selected value=\"" + subjects[i].id + "\">" + subjects[i].name_subject_RF + "</option>";
        } else {
            newHtml = newHtml + "<option value=\"" + subjects[i].id + "\">" + subjects[i].name_subject_RF + "</option>";
        }
    }

    subjectNode.innerHTML = newHtml;

    await setOptionInForestly(MergeStatementRecalculationsBusiness.TypeData.BYID);
}

async function setOptionInForestly(status) {
    let forestlyNode = document.querySelector("#filter_forestly");
    let forestly;

    if(status == MergeStatementRecalculationsBusiness.TypeData.BYID) {
        let subjectNode = document.querySelector("#filter_subject_rf");
        forestly = await CommonBusiness.getForestlyByIdSubjectrf(subjectNode.value);
    } else {
        forestly = APP.forestly;
    }

    var newHtml = "";

    for(var i = 0; i < forestly.length; i++) {
        if(i == 0) {
            newHtml = newHtml + "<option selected value=\"" + forestly[i].id + "\">" + forestly[i].name_forestly + "</option>";
        } else {
            newHtml = newHtml + "<option value=\"" + forestly[i].id + "\">" + forestly[i].name_forestly + "</option>";
        }
    }
    forestlyNode.innerHTML = newHtml;

    await setOptionInDistrictForestly(MergeStatementRecalculationsBusiness.TypeData.BYID);
}

async function setOptionInDistrictForestly(status) {
    let districtForestlyNode = document.querySelector("#filter_district_forestly");
    let districtForestly;

    if(status == MergeStatementRecalculationsBusiness.TypeData.BYID) {
        let forestlyNode = document.querySelector("#filter_forestly");
        districtForestly = await CommonBusiness.getDistrictForestlyByIdForestly(forestlyNode.value);
    } else {
        districtForestly = APP.district_forestly;
    }

    var newHtml = "";

    for(var i = 0; i < districtForestly.length; i++) {
        if(i == 0) {
            newHtml = newHtml + "<option selected value=\"" + districtForestly[i].id + "\">" + districtForestly[i].name_district_forestly + "</option>";
        } else {
            newHtml = newHtml + "<option value=\"" + districtForestly[i].id + "\">" + districtForestly[i].name_district_forestly + "</option>";
        }
    }

    districtForestlyNode.innerHTML = newHtml;

    await setOptionInQuarter(MergeStatementRecalculationsBusiness.TypeData.BYID);
}

async function setOptionInQuarter(status) {

    let quarterNode = document.querySelector("#filter_quartal");
    let quarter;

    if(status == MergeStatementRecalculationsBusiness.TypeData.BYID) {
        let districtForestlyNode = document.querySelector("#filter_district_forestly");
        quarter = await CommonBusiness.getQuarterByIdDistrictForestly(districtForestlyNode.value);
    } else {
        quarter = APP.quarter;
    }

    var newHtml = "";
    for(var j = 0; j < quarter.length; j++) {
        if(j == 0) {
            newHtml = newHtml + "<option selected value=\"" + quarter[j].id + "\">" + quarter[j].quarter_name + "</option>";
        } else {
            newHtml = newHtml + "<option value=\"" + quarter[j].id + "\">" + quarter[j].quarter_name + "</option>";
        }
    }
    quarterNode.innerHTML = newHtml;
}

async function searchByFilter() {

    let checkboxFilterSubjectRFNode = document.querySelector("#checkbox_filter_subject_rf");
    let subjectRFNode = document.querySelector("#filter_subject_rf");
    let checkboxFilterForestlyNode = document.querySelector("#checkbox_filter_forestly");
    let forestlyNode = document.querySelector("#filter_forestly");
    let checkboxFilterDistrictForestlyNode = document.querySelector("#checkbox_filter_district_forestly");
    let districtForestlyNode = document.querySelector("#filter_district_forestly");
    let checkboxFilterQuartalNode = document.querySelector("#checkbox_filter_quartal");
    let quartalNode = document.querySelector("#filter_quartal")
    let checkboxFilterDateStartNode = document.querySelector("#checkbox_filter_date_start");
    let dateStartNode = document.querySelector("#filter_date_start");
    let checkboxFilterDateEnd = document.querySelector("#checkbox_filter_date_end");
    let dateEndNode = document.querySelector("#filter_date_end");

    let data;

    if(checkboxFilterSubjectRFNode.checked || checkboxFilterForestlyNode.checked
    || checkboxFilterDistrictForestlyNode.checked || checkboxFilterQuartalNode.checked
    || checkboxFilterDateStartNode.checked || checkboxFilterDateEnd.checked) {

        let responseData = {
            bSubjectrf: checkboxFilterSubjectRFNode.checked,
            idSubjectrf: subjectRFNode.value,
            bForestly: checkboxFilterForestlyNode.checked,
            idForestly: forestlyNode.value,
            bDistrictForestly: checkboxFilterDistrictForestlyNode.checked,
            idDistrictForestly: districtForestlyNode.value,
            bQuarter: checkboxFilterQuartalNode.checked,
            idQuarter: quartalNode.value,
            bDate: checkboxFilterDateStartNode.checked,
            date: dateStartNode.value,
            bDateSec: checkboxFilterDateEnd.checked,
            dateSec: dateEndNode.value
        };


        data = await MergeStatementRecalculationsBusiness.getCreateRecalculationDetailData(responseData);
    } else {

        data = await MergeStatementRecalculationsBusiness.getAllStatementList();
    }


    updateDataInStatementRecalculationsTbody(data);
}

function addOrRemoveActiveItemTr(id) {

    if(APP.idActiveItemTr.indexOf(id) == -1) {
        APP.idActiveItemTr.push(id);
        document
            .querySelector("#statement_" + id)
            .classList.add("activeTr");
    } else {
        let buff = APP.idActiveItemTr;
        APP.idActiveItemTr = [];

        for(let i = 0; i < buff.length; i++) {
            if(buff[i] != id) {
                APP.idActiveItemTr.push(buff[i]);
            }
        }

        document
            .querySelector("#statement_" + id)
            .classList.remove("activeTr");
    }

}