// fetch("https://apps.who.int/gho/athena/api/?format=json")
//=========================================
//declayeration of all global variables for accessing all incoming data
// let new_total_case = [];
// let new_total_deaths = [];
// let new_total_recoveries = [];
// let date1 = [];
// let total_case1 = [];
// let new_total_case = [];
// let new_total_case = [];
//================================


//============================================================================
fetch("https://api.rootnet.in/covid19-in/stats/history")
	.then(response => response.json())
	.then(res => {
		console.log(res);
		let total_case1 = [];
		let last_total_case1 = 0;
		let date1 = [];
		//-----------------------
		let total_death1 = [];
		let last_total_death1 = 0;
		//-----------------------
		let total_dischaged1 = [];
		let last_total_discharged1 = 0;
		//-----------------------
		let tot=[],dis=[],deth=[];
		//-----------------------
		res['data'].forEach(element => {
			let t = element['summary']['total'];
			tot.push(parseFloat(t));
			total_case1.push(parseFloat(t) - last_total_case1);
			last_total_case1 = parseFloat(t);
			let day = element['day'];
			date1.push(day);
			//---------------------------------------------
			let d = element['summary']['deaths'];
			deth.push(parseFloat(d));
			total_death1.push(parseFloat(d) - last_total_death1);
			last_total_death1 = parseFloat(d);

			//---------------------------------------------
			let r = element['summary']['discharged'];
			dis.push(parseFloat(r));
			total_dischaged1.push(parseFloat(r) - last_total_discharged1);
			last_total_discharged1 = parseFloat(r);

			//---------------------------------------------
		});

		//==============ichart1===============
		const ctx = document.getElementById('ichart1').getContext('2d');
		const myChart1 = new Chart(ctx, {
			type: 'line',
			data: {
				labels: date1,
				datasets: [
					{
					label: 'no of new cases',
					data: total_case1,
					borderColor: 'rgb(255, 0, 0)',
					// backgroundColor: 'rgb(252, 237, 237  )',
					// fill: true,
				},
				{
					label: 'no of persons discharged',
					data: total_dischaged1,
					borderColor: 'rgb(46, 46, 245)',
					// backgroundColor: 'rgb(252, 237, 237  )',
					// fill: true,
				},
				{
					label: 'no of deaths',
					data: total_death1,
					borderColor: 'rgb(0, 0, 0)',
					// backgroundColor: 'rgb(252, 237, 237  )',
					// fill: true,
				}
			]
			},
			options: {
				interaction: {
					intersect: false,
					mode: 'index',
				},
				radius: 0,
				elements: {
					line: {
						tension: 0
					}
				},
				scales: {
					x: {
						display: true,
						grid: { drawBorder: true, lineWidth: 0, drawOnChartArea: false },
						title: {
							display: true,
							text: 'date'
						}
					},
					y: {

						position: 'right',
						display: true,
						// type: 'logarithmic',
						grid: { drawBorder: true, lineWidth: 0, drawOnChartArea: false },
						beginAtZero: true,
						title: {
							display: false,
							text: 'no of cases'
						},
						min: 0,
						//max: 100,
						// ticks: {
						// 	// forces step size to be 50 units
						// 	stepSize: 50000
						// }
					}
				}
			}
		});
		//======================ichart2==========================
		const ct2 = document.getElementById('ichart2').getContext('2d');
		const myChart2 = new Chart(ct2, {
			type: 'line',
			data: {
				labels: date1,
				datasets: [
					{
					label: 'total no of cases',
					data: tot,
					borderColor: 'rgb(255, 0, 0)',
					// backgroundColor: 'rgb(252, 237, 237  )',
					// fill: true,
				},
				{
					label: 'total no of persons discharged',
					data: dis,
					borderColor: 'rgb(46, 46, 245)',
					// backgroundColor: 'rgb(252, 237, 237  )',
					// fill: true,
				},
				{
					label: 'total no of deaths',
					data: deth,
					borderColor: 'rgb(0, 0, 0)',
					// backgroundColor: 'rgb(252, 237, 237  )',
					// fill: true,
				}
			]
			},
			options: {
				interaction: {
					intersect: false,
					mode: 'index',
				},
				radius: 0,
				elements: {
					line: {
						tension: 0
					}
				},
				scales: {
					x: {
						display: true,
						grid: { drawBorder: true, lineWidth: 0, drawOnChartArea: false },
						title: {
							display: true,
							text: 'date'
						}
					},
					y: {

						position: 'right',
						display: true,
						// type: 'logarithmic',
						grid: { drawBorder: true, lineWidth: 0, drawOnChartArea: false },
						beginAtZero: true,
						title: {
							display: false,
							text: 'no of cases'
						},
						min: 0,
						//max: 100,
						// ticks: {
						// 	// forces step size to be 50 units
						// 	stepSize: 50000
						// }
					}
				}
			}
		});


	})
	.catch(err => {
		console.error(err);
	});
////========================
////=========================
////=========================
fetch("https://api.rootnet.in/covid19-in/stats/testing/history")
	.then(r1 => r1.json())
	.then(res1 => {
		console.log(res1);
		let date2=[];
		let tests=[];
		let cumtests=[];
		let ct=0;
		let prevct=0;
		res1['data'].forEach(element => {
			let day = element['day'];
			date2.push(day);
			ct = element['totalSamplesTested'];
			cumtests.push(ct);
			tests.push(parseFloat(ct) - prevct);
			prevct=ct;
		} )
		const ct3 = document.getElementById('tchart1').getContext('2d');
		const myChart3 = new Chart(ct3, {
			type: 'bar',
			data: {
				labels: date2,
				datasets: [
					{
					label: 'no of tests done',
					data: tests,
					borderColor: 'rgb(255, 0, 0)',
					backgroundColor: 'rgb(255, 0, 0)',
					fill: true,
				}
			]
			},
			options: {
				interaction: {
					intersect: false,
					mode: 'index',
				},
				radius: 0,
				// elements: {
				// 	line: {
				// 		tension: 0
				// 	}
				// },
				scales: {
					x: {
						display: true,
						grid: { drawBorder: true, lineWidth: 0, drawOnChartArea: false },
						title: {
							display: true,
							text: 'date'
						}
					},
					y: {

						position: 'right',
						display: true,
						// type: 'logarithmic',
						grid: { drawBorder: true, lineWidth: 0, drawOnChartArea: false },
						beginAtZero: true,
						title: {
							display: false,
							text: 'no of persons tested'
						},
						min: 0,
					}
				}
			}
		});
	})
	.catch(err => {
		console.error(err);
	});

///============================
///============================
///============================
fetch("https://api.rootnet.in/covid19-in/stats/history")
	.then(r2 => r2.json())
	.then(res2 => {
		console.log(res2);
		let location=[];
		let len = res2['data'].length;
		let pcases=[],ncases=[],pdeath=[],ndeath=[],prec=[],nrec=[];
		res2['data'][len-1]['regional'].forEach(element => {
			let locat = element['loc'];
			location.push(locat);
		} )
		res2['data'][len-2]['regional'].forEach(element => {
			let pc = element['confirmedCasesIndian'];
			pcases.push(parseFloat(pc));
			let pd = element['deaths'];
			pdeath.push(parseFloat(pd));
			let pr = element['discharged'];
			prec.push(parseFloat(pr));
		} )
		res2['data'][len-1]['regional'].forEach(element => {
			let nc = element['confirmedCasesIndian'];
			ncases.push(parseFloat(nc));
			let nd = element['deaths'];
			ndeath.push(parseFloat(nd));
			let nr = element['discharged'];
			nrec.push(parseFloat(nr));
		} )
		let cas=[],det=[],re=[];
		for (let step = 0; step < 36; step++) {
			cas.push(ncases[step]-pcases[step]);
			det.push(ndeath[step]-pdeath[step]);
			re.push(nrec[step]-prec[step]);
		  }
		
		const ct4 = document.getElementById('schart1').getContext('2d');
		const myChart4 = new Chart(ct4, {
			type: 'bar',
			data: {
				labels: location,
				datasets: [
				{
					label: 'no of new cases',
					data: cas,
					borderColor: 'rgb(0, 0, 255)',
					backgroundColor: 'rgb(0, 0, 255)',
					fill: true,
				},
				{
					label: 'no of patients recovered',
					data: re,
					borderColor: 'rgb(0, 255, 0)',
					backgroundColor: 'rgb(0, 255, 0)',
					fill: true,
				},
				{
					label: 'no of deaths',
					data: det,
					borderColor: 'rgb(255, 0, 0)',
					backgroundColor: 'rgb(255, 0, 0)',
					fill: true,
				}
			]
			},
			options: {
				interaction: {
					intersect: false,
					mode: 'index',
				},
				radius: 0,
				// elements: {
				// 	line: {
				// 		tension: 0
				// 	}
				// },
				scales: {
					x: {
						stacked: true,
						display: true,
						grid: { drawBorder: true, lineWidth: 0, drawOnChartArea: false },
						title: {
							display: true,
							text: 'regions'
						}
					},
					y: {
						stacked: true,
						position: 'right',
						display: true,
						// type: 'logarithmic',
						grid: { drawBorder: true, lineWidth: 0, drawOnChartArea: false },
						beginAtZero: true,
						title: {
							display: false,
							text: 'no of persons tested'
						},
						min: 0,
					}
				}
			}
		});
	})
	.catch(err => {
		console.error(err);
	});