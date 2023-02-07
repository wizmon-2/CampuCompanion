import * as React from 'react';
import Avatar from '@mui/material/Avatar';
import Button from '@mui/material/Button';
import CssBaseline from '@mui/material/CssBaseline';
import TextField from '@mui/material/TextField';
import FormControlLabel from '@mui/material/FormControlLabel';
import Checkbox from '@mui/material/Checkbox';
import Link from '@mui/material/Link';
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import LockOutlinedIcon from '@mui/icons-material/LockOutlined';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import { useState } from 'react';

const theme = createTheme();

export default function SignIn() {
  
  const[errors, setErrors] = useState(false);
  const[loading, setLoading] = useState(false);

  const handleSubmit = (event) => {
    event.preventDefault();
    const data = new FormData(event.currentTarget);

    setLoading(true);

    const userid = data.get('userid');
    const password = data.get('password');

    const requestOptions = {
			method : 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
			body : JSON.stringify({
				userid : userid,
				password : password
			}),
		};

    fetch('http://127.0.0.1:8000/api/login/', requestOptions)
			.then((response) => response.json())
			.then( (data) => storeit(data));

      let storeit = (data) => {

        if(data.Error == "Does Not Exist")
        {
          setLoading(false);
          setErrors(true);
        }

        if(data.user)
        {
          setErrors(false);

          localStorage.setItem("token", data.token);
          localStorage.setItem("iid", data.user.iid);
          localStorage.setItem("userid", data.user.userid);
          localStorage.setItem("user_type", data.user.user_type);
          localStorage.setItem("name", data.user.name);
        }

      }

	  
  };

  return (
    <ThemeProvider theme={theme}>
      <Container component="main" maxWidth="xs">
        <CssBaseline />
        <Box
          sx={{
            marginTop: 8,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
          }}
        >
          { loading === false &&
          <Avatar sx={{ m: 1, bgcolor: 'secondary.main' }}>
            <LockOutlinedIcon />
          </Avatar>
          }
          { loading === false &&
          <Typography component="h1" variant="h5">
            Sign in
          </Typography>
          }
          {errors === true && <p>Cannot log in with provided credentials</p> }
          {loading === false &&
          <Box component="form" onSubmit={handleSubmit} noValidate sx={{ mt: 1 }}>
            <TextField
              margin="normal"
              required
              fullWidth
              id="userid"
              label="User ID"
              name="userid"
              autoComplete="userid"
              autoFocus
            />
            <TextField
              margin="normal"
              required
              fullWidth
              name="password"
              label="Password"
              type="password"
              id="password"
              autoComplete="current-password"
            />
            <Button
              type="submit"
              fullWidth
              variant="contained"
              sx={{ mt: 3, mb: 2 }}
            >
              Sign In
            </Button>
          </Box> }
        </Box>
      </Container>
    </ThemeProvider>
  );
}
