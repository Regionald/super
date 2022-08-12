
function downloadPDF(id) {
    const element = document.getElementById(id).outerHTML;
    // element.setAttribute('width','50px');
  // html2pdf().from(element).save();
    console.log(element);
    html2pdf().from(element).set({
        margin:       [1, 0, 0, 0], 
          filename: 'invoice.pdf',
            pageBreak: { mode: 'css', before:'#nextpage1'},
          jsPDF: {orientation: 'landscape', unit: 'in', format: 'letter'}
        }).toPdf().get('pdf').then(function (pdf) {
          var totalPages = pdf.internal.getNumberOfPages();
      
          for (i = 1; i <= totalPages; i++) {
              pdf.setPage(i);
            pdf.setFontSize(10);
            pdf.setTextColor(150);
          pdf.text('Page ' + i + ' of ' + totalPages, (pdf.internal.pageSize.getWidth()/2.25), (pdf.internal.pageSize.getHeight()-8));
            
           
            }
        }).save();

}
