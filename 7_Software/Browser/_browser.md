- Расширения браузера
	- AutoControl: Keyboard shortcuts, Mouse gestures
		- Открывать первую вкладку гугл при открытии страница гугл
			const w = document.querySelector(".zReHs");
			// alert(w.href) ;
			window.open(w.href, '_blank').focus();
			//	window.location.replace(w.href)
		- Закрывать пустые вкладки при открытии новых