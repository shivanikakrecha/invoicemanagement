$( document ).ready(function() {
  $("#input-pd").fileinput({
	    uploadUrl: "/file-upload-batch/1",
	    uploadAsync: false,
	}).on('filesorted', function(e, params) {
	    console.log('File sorted params', params);
	}).on('fileuploaded', function(e, params) {
	    console.log('File uploaded params', params);
	});

	$('.parent-file-loading').on('click', function(){
		setTimeout(function () { 
			$('.file-caption-main').hide() 
		}, 2000);

		$('#remove-file-loading').show();

	})

	$('#remove-file-loading').on('click', function(){
		$('#remove-file-loading').hide();
		$('.file-caption-main').show() 
	})

	// If absolute URL from the remote server is provided, configure the CORS
	// header on that server.
	function InvoiceCreateFilePreview(file){
		var url = file

		// Loaded via <script> tag, create shortcut to access PDF.js exports.
		var pdfjsLib = window['pdfjs-dist/build/pdf'];

		// The workerSrc property shall be specified.
		pdfjsLib.GlobalWorkerOptions.workerSrc = '//mozilla.github.io/pdf.js/build/pdf.worker.js';

		var pdfDoc = null,
		    pageNum = 1,
		    pageRendering = false,
		    pageNumPending = null,
		    scale = 0.8,
		    canvas = document.getElementById('the-canvas'),
		    ctx = canvas.getContext('2d');

		/**
		 * Get page info from document, resize canvas accordingly, and render page.
		 * @param num Page number.
		 */
		function renderPage(num) {
		  pageRendering = true;
		  // Using promise to fetch the page
		  pdfDoc.getPage(num).then(function(page) {
		    var viewport = page.getViewport({scale: scale});
		    canvas.height = viewport.height;
		    canvas.width = viewport.width;

		    // Render PDF page into canvas context
		    var renderContext = {
		      canvasContext: ctx,
		      viewport: viewport
		    };
		    var renderTask = page.render(renderContext);

		    // Wait for rendering to finish
		    renderTask.promise.then(function() {
		      pageRendering = false;
		      if (pageNumPending !== null) {
		        // New page rendering is pending
		        renderPage(pageNumPending);
		        pageNumPending = null;
		      }
		    });
		  });

		  // Update page counters
		  document.getElementById('page_num').textContent = num;
		}

		/**
		 * If another page rendering in progress, waits until the rendering is
		 * finised. Otherwise, executes rendering immediately.
		 */
		function queueRenderPage(num) {
		  if (pageRendering) {
		    pageNumPending = num;
		  } else {
		    renderPage(num);
		  }
		}

		/**
		 * Displays previous page.
		 */
		function onPrevPage() {
		  if (pageNum <= 1) {
		    return;
		  }
		  pageNum--;
		  queueRenderPage(pageNum);
		}
		document.getElementById('prev').addEventListener('click', onPrevPage);

		/**
		 * Displays next page.
		 */
		function onNextPage() {
		  if (pageNum >= pdfDoc.numPages) {
		    return;
		  }
		  pageNum++;
		  queueRenderPage(pageNum);
		}
		document.getElementById('next').addEventListener('click', onNextPage);

		/**
		 * Asynchronously downloads PDF.
		 */
		pdfjsLib.getDocument(url).promise.then(function(pdfDoc_) {
		  pdfDoc = pdfDoc_;
		  document.getElementById('page_count').textContent = pdfDoc.numPages;

		  renderPage(pageNum);
		});
	}

	$('#id_attachment').on('change',function ()
        {
            var filePath = $(this).val();
            var input = document.getElementById("id_attachment");
			var fReader = new FileReader();
			fReader.readAsDataURL(input.files[0]);
			fReader.onloadend = function(event){
			    InvoiceCreateFilePreview(event.target.result)
			}
        });
});