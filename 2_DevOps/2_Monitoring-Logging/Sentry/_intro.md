# 
	- https://dev.to/gbengacode/how-to-monitor-nextjs-application-performance-and-track-errors-with-sentry-36l2
		
    try {

       throw new Error("this is an error")

    } catch (error) {

      Sentry.captureException(error)

    }

- отправить
	https://docs.sentry.io/platforms/javascript/usage/
	Sentry.captureMessage("Something went wrong");
