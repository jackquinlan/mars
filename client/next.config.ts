import { NextConfig } from "next";

const nextConfig: NextConfig = {
  reactStrictMode: true,
  rewrites: async () => {
    return [
      {
        source: '/api/chess/:path*', // route all 'chess' api calls
        destination:
          process.env.NODE_ENV === 'development'
            ? 'http://127.0.0.1:5000/api/chess/:path*'
            : '/api/chess',
      },
    ]
  },
};

export default nextConfig;

