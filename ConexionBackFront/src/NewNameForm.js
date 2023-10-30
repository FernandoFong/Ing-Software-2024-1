import { useState } from "react";


function NewNameForm (props) {
    const [enteredName, setName] = useState('');
    const [enteredLastName, setLastName] = useState('');

    const nameChangeHandler = (event) => {
        setName(event.target.value);
    }

    const lastNameChangeHandler = (event) => {
        setLastName(event.target.value);
    }

    const submitHandler = (event) => {
        event.preventDefault();

        const newName = {
            name:enteredName,
            last_name:enteredLastName
        }
        props.onSaveName(newName);
        setName('');
        setLastName('');
    }

    return (
        <form onSubmit={submitHandler}>
            <div>
                <label>Name: </label>
                <input 
                    type='text'
                    value={enteredName}
                    onChange={nameChangeHandler}
                />
            </div>
            <div>
                <label>Last Name: </label>
                <input
                    type='text'
                    value={enteredLastName}
                    onChange={lastNameChangeHandler}
                />
            </div>
            <div>
                <button type="submit">Add Name</button>
            </div>
        </form>
    )
}

export default NewNameForm;