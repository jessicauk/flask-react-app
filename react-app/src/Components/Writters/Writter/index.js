import React, { Fragment } from 'react';

export default ({ match, name, description, born,deceased, image}) =>
  <Fragment>
    <img src={image} alt={name} style={{maxWidth: '300px'}}/>
    <h1>{name}</h1>
    <h3>{born} &ndash; {deceased} </h3>
    <p>{description}</p>
  </Fragment>