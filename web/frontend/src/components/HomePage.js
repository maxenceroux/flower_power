import React, { Component } from "react";
import { Grid, Button, ButtonGroup, Typography } from "@material-ui/core";
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  Redirect,
} from "react-router-dom";

export default class HomePage extends Component {
  constructor(props) {
    super(props);
  }
  renderHomePage() {
    return (
        <Grid container spacing={3}>
            <Grid item xs={12} align="center">
                <Typography variant="h1" compact="h1">
                    Unleash the flower power
                </Typography>
            </Grid>
            <Grid item xs={12} align="center">
                <Button color="primary" to="/create" component={Link}>
                    Create a flower
                </Button>
            </Grid>
        </Grid>
    )
  }
}
