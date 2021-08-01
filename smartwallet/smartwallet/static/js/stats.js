
const renderChart = (data1, labels1) =>{
    
    var ctx = document.getElementById('myChart').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'doughnut',
    data: {
        labels: labels1,
        datasets: [{
            label: 'Last 6 months expenses',
            data: data1,
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        title:{
            display: true,
            text:'Expenses per Category'
        }
       
    }
});

}

const getChartData=() =>{
    console.log('areee')
    fetch('expense_catogory_summary')
    .then(res=>res.json())
    .then((results)=>{
        console.log('results', results)

        const category_data = results.expense_catogory_data;
        const[labels1,data1] = [Object.keys(category_data), Object.values(category_data)];
        renderChart(data1, labels1);
        

    })
}
document.onload=getChartData();