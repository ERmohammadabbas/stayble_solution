import { spawn } from 'child_process';

console.log('🚀 Starting Django E-Commerce Application...');
console.log('============================================');

const djangoServer = spawn('python', ['manage.py', 'runserver', '0.0.0.0:5000'], {
  stdio: 'inherit',
  cwd: process.cwd()
});

djangoServer.on('error', (error) => {
  console.error('Failed to start Django server:', error);
  process.exit(1);
});

djangoServer.on('exit', (code) => {
  console.log(`Django server exited with code ${code}`);
  process.exit(code || 0);
});

process.on('SIGINT', () => {
  console.log('\nShutting down Django server...');
  djangoServer.kill('SIGINT');
});

process.on('SIGTERM', () => {
  djangoServer.kill('SIGTERM');
});
