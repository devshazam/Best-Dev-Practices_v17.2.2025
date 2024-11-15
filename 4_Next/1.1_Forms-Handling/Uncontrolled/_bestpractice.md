обычная HTML-форма работала бы без JavaScript.<form>

function UncontrolledForm() {

  const handleSubmit = (event) => {
    event.preventDefault();

    const formData = new FormData(event.target);
    const inputValue = formData.get('inputName');

    sendInputValueToApi(inputValue).then(() => /* Do something */)  
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="text" name="inputName" />
      <button type="submit">Send</button>
    </form>
  );