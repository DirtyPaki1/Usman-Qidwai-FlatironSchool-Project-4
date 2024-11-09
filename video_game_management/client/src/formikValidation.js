import React from 'react';
import { useFormik } from 'formik';
import * as Yup from 'yup';
import { addGame } from './api';

const AddGameForm = () => {
    const formik = useFormik({
        initialValues: {
            name: '',
            release_date: '',
            price: '',
            genre_id: ''
        },
        validationSchema: Yup.object({
            name: Yup.string().required('Game name is required'),
            release_date: Yup.date().required('Release date is required'),
            price: Yup.number().required('Price is required'),
            genre_id: Yup.number().required('Genre is required')
        }),
        onSubmit: async (values) => {
            await addGame(values);
        }
    });

    return (
        <form onSubmit={formik.handleSubmit}>
            <div>
                <label>Name</label>
                <input
                    type="text"
                    name="name"
                    onChange={formik.handleChange}
                    value={formik.values.name}
                />
                {formik.errors.name ? <div>{formik.errors.name}</div> : null}
            </div>
            {/* Add other fields like release_date, price, genre_id */}
            <button type="submit">Add Game</button>
        </form>
    );
};

export default AddGameForm;
